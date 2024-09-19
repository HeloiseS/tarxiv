"""Pull and process lightcurves"""

import logging

_LOG = logging.getLogger(__name__)


def mapping_ztf_to_tarxiv():
    """Mapping between ZTF column names and tarxiv column names

    Returns
    -------
    dict
        Dictionary containing mapping between
        Fink column names and tarxiv column names
    """
    # TODO: define tarxiv column names
    dic = {
        "i:magpsf": "MAG",
        "i:sigmapsf": "MAGERR",
        "i:fid": "FILTER",
        "i:jd": "TIME",
        "whatelse?": "TBD",
    }

    return dic


def get_ztf_lc(ztf_name=None, tns_name=None, coord=None):
    """Get data from ZTF based on either name or coordinates

    Parameters
    ----------
    ztf_name: str
        Name of a ZTF object, starting with `ZTF`
    tns_name: str
        Name of an object in TNS
    coord: tuple of float
        Object coordinates (RA, Dec), in degrees

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing ZTF data from Fink for
        the matching object in TNS. Each row is a measurement.

    """
    if ztf_name is not None:
        pdf = get_ztf_lc_from_ztf_name(ztf_name)
    elif tns_name is not None:
        pdf = get_ztf_lc_from_tns_name(tns_name)
    elif coord is not None and isinstance(coord, tuple):
        pdf = get_ztf_lc_from_coord(coord[0], coord[1])
    else:
        _LOG.error(
            "You should choose an object name or provide coordinates to get ZTF lightcurves"
        )

    # TODO: perform the column name conversion before returning
    # TODO: `mapping_ztf_to_tarxiv`
    return pdf


def get_ztf_lc_from_ztf_name(ztf_name: str):
    pass


def get_ztf_lc_from_tns_name(tns_name: str):
    pass


def get_ztf_lc_from_coord(ra: float, dec: float):
    pass
