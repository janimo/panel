from collections import namedtuple

SCALAR_MODE = namedtuple("SCALAR_MODE",
    "Default UsePointData UseCellData UsePointFieldData UseCellFieldData UseFieldData"
)(0, 1, 2, 3, 4, 5)

COLOR_MODE = namedtuple("COLOR_MODE", "DirectScalars MapScalars")(0, 1)

ACCESS_MODE = namedtuple("ACCESS_MODE", "ById ByName")(0, 1)

PRESET_CMAPS = [
    '2hot',
    'Asymmtrical Earth Tones (6_21b)',
    'BLUE-WHITE',
    'BkBu',
    'BkCy',
    'BkGn',
    'BkMa',
    'BkRd',
    'Black, Blue and White',
    'Black, Orange and White',
    'Black-Body Radiation',
    'Blue to Red Rainbow',
    'Blue to Yellow',
    'Blues',
    'BrBG',
    'BrOrYl',
    'BuGn',
    'BuGnYl',
    'BuPu',
    'BuRd',
    'CIELab Blue to Red',
    'CIELab_blue2red',
    'Cold and Hot',
    'Cool to Warm',
    'Cool to Warm (Extended)',
    'GBBr',
    'GREEN-WHITE_LINEAR',
    'GYPi',
    'GnBu',
    'GnBuPu',
    'GnRP',
    'GnYlRd',
    'Grayscale',
    'Green-Blue Asymmetric Divergent (62Blbc)',
    'Greens',
    'GyRd',
    'Haze',
    'Haze_cyan',
    'Haze_green',
    'Haze_lime',
    'Inferno (matplotlib)',
    'Linear Blue (8_31f)',
    'Linear YGB 1211g',
    'Magma (matplotlib)',
    'Muted Blue-Green',
    'OrPu',
    'Oranges',
    'PRGn',
    'PiYG',
    'Plasma (matplotlib)',
    'PuBu',
    'PuOr',
    'PuRd',
    'Purples',
    'RED-PURPLE',
    'RED_TEMPERATURE',
    'Rainbow Blended Black',
    'Rainbow Blended Grey',
    'Rainbow Blended White',
    'Rainbow Desaturated',
    'RdOr',
    'RdOrYl',
    'RdPu',
    'Red to Blue Rainbow',
    'Reds',
    'Spectral_lowBlue',
    'Viridis (matplotlib)',
    'Warm to Cool',
    'Warm to Cool (Extended)',
    'X Ray',
    'Yellow 15',
    'blot',
    'blue2cyan',
    'blue2yellow',
    'bone_Matlab',
    'coolwarm',
    'copper_Matlab',
    'erdc_blue2cyan_BW',
    'erdc_blue2gold',
    'erdc_blue2gold_BW',
    'erdc_blue2green_BW',
    'erdc_blue2green_muted',
    'erdc_blue2yellow',
    'erdc_blue_BW',
    'erdc_brown_BW',
    'erdc_cyan2orange',
    'erdc_divHi_purpleGreen',
    'erdc_divHi_purpleGreen_dim',
    'erdc_divLow_icePeach',
    'erdc_divLow_purpleGreen',
    'erdc_gold_BW',
    'erdc_green2yellow_BW',
    'erdc_iceFire_H',
    'erdc_iceFire_L',
    'erdc_magenta_BW',
    'erdc_marine2gold_BW',
    'erdc_orange_BW',
    'erdc_pbj_lin',
    'erdc_purple2green',
    'erdc_purple2green_dark',
    'erdc_purple2pink_BW',
    'erdc_purple_BW',
    'erdc_rainbow_bright',
    'erdc_rainbow_dark',
    'erdc_red2purple_BW',
    'erdc_red2yellow_BW',
    'erdc_red_BW',
    'erdc_sapphire2gold_BW',
    'gist_earth',
    'gray_Matlab',
    'heated_object',
    'hsv',
    'hue_L60',
    'jet',
    'magenta',
    'nic_CubicL',
    'nic_CubicYF',
    'nic_Edge',
    'pink_Matlab',
    'rainbow'
]
