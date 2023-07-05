from .baseline import BaselinePredictor
from .focalclick import FocalPredictor
from .focalclick_draw import FocalPredictorDraw
from .ours_predictor import NoRefinePredictor
from .ours_predictor_Draw import NoRefinePredictorDraw
from .brs import InputBRSPredictor, FeatureBRSPredictor, HRNetFeatureBRSPredictor
from .brs_functors import InputOptimizer, ScaleBiasOptimizer
from isegm.inference.transforms import ZoomIn


def get_predictor(net, brs_mode, device,
                  prob_thresh=0.49,
                  infer_size=256,
                  focus_crop_r=1.4,
                  with_flip=False,
                  zoom_in_params=dict(),
                  predictor_params=None,
                  brs_opt_func_params=None,
                  lbfgs_params=None):
    lbfgs_params_ = {
        'm': 20,
        'factr': 0,
        'pgtol': 1e-8,
        'maxfun': 20,
    }

    predictor_params_ = {
        'optimize_after_n_clicks': 1
    }

    if zoom_in_params is not None:
        zoom_in = ZoomIn(**zoom_in_params)
    else:
        zoom_in = None

    if lbfgs_params is not None:
        lbfgs_params_.update(lbfgs_params)
    lbfgs_params_['maxiter'] = 2 * lbfgs_params_['maxfun']

    if brs_opt_func_params is None:
        brs_opt_func_params = dict()

    if isinstance(net, (list, tuple)):
        assert brs_mode == 'NoBRS', "Multi-stage models support only NoBRS mode."

    if brs_mode == 'NoBRS':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = BaselinePredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                      **predictor_params_)

    elif brs_mode == 'CDNet':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = DiffisionPredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                       **predictor_params_)

    elif brs_mode == 'FocalClick':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = FocalPredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                   focus_crop_r=focus_crop_r, **predictor_params_)

    elif brs_mode == 'Baseline':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = BaselinePredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                      **predictor_params_)

    elif brs_mode == 'FocalClickDraw':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = FocalPredictorDraw(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                       focus_crop_r=focus_crop_r, **predictor_params_)

    elif brs_mode == 'NoRefine':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = NoRefinePredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                       focus_crop_r=focus_crop_r, **predictor_params_)
    elif brs_mode == 'NoRefineCascade':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = CascadePredictor(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                       focus_crop_r=focus_crop_r, **predictor_params_)

    elif brs_mode == 'NoRefineDraw':
        if predictor_params is not None:
            predictor_params_.update(predictor_params)
        predictor = NoRefinePredictorDraw(net, device, zoom_in=zoom_in, with_flip=with_flip, infer_size=infer_size,
                                       focus_crop_r=focus_crop_r, **predictor_params_)

    elif brs_mode.startswith('f-BRS'):
        predictor_params_.update({
            'net_clicks_limit': 8,
        })
        if predictor_params is not None:
            predictor_params_.update(predictor_params)

        insertion_mode = {
            'f-BRS-A': 'after_c4',
            'f-BRS-B': 'after_aspp',
            'f-BRS-C': 'after_deeplab'
        }[brs_mode]

        opt_functor = ScaleBiasOptimizer(prob_thresh=prob_thresh,
                                         with_flip=with_flip,
                                         optimizer_params=lbfgs_params_,
                                         **brs_opt_func_params)

        FeaturePredictor = FeatureBRSPredictor

        predictor = FeaturePredictor(net, device,
                                     opt_functor=opt_functor,
                                     with_flip=with_flip,
                                     insertion_mode=insertion_mode,
                                     zoom_in=zoom_in,
                                     **predictor_params_)
    elif brs_mode == 'RGB-BRS' or brs_mode == 'DistMap-BRS':
        use_dmaps = brs_mode == 'DistMap-BRS'

        predictor_params_.update({
            'net_clicks_limit': 5,
        })
        if predictor_params is not None:
            predictor_params_.update(predictor_params)

        opt_functor = InputOptimizer(prob_thresh=prob_thresh,
                                     with_flip=with_flip,
                                     optimizer_params=lbfgs_params_,
                                     **brs_opt_func_params)

        predictor = InputBRSPredictor(net, device,
                                      optimize_target='dmaps' if use_dmaps else 'rgb',
                                      opt_functor=opt_functor,
                                      with_flip=with_flip,
                                      zoom_in=zoom_in,
                                      **predictor_params_)
    else:
        raise NotImplementedError

    return predictor
