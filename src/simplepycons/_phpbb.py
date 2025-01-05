#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class PhpbbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phpbb"

    @property
    def original_file_name(self) -> "str":
        return "phpbb.svg"

    @property
    def title(self) -> "str":
        return "phpBB"

    @property
    def primary_color(self) -> "str":
        return "#009BDF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>phpBB</title>
     <path d="M4.5826 11.9021q0 .5784-.1424 1.0634t-.4137.8409a1.85
 1.85 0 0 1-.6763.5516q-.405.1959-.9299.1958-.4005
 0-.7163-.2002t-.4938-.5117v2.1178H.8364a.87.87 0 0
 1-.3114-.0578.82.82 0 0 1-.267-.1646.83.83 0 0 1-.1868-.258Q0 15.3278
 0
 15.1321v-2.9008q0-.5962.138-1.0945.1378-.4983.4315-.8543t.7474-.5517q.4539-.1957
 1.0856-.1957.4805 0
 .881.2002.4005.2003.6896.5294.2892.3292.4493.7564.1602.427.1602.881m-1.228.3115q0-.8542-.2802-1.2369-.2804-.3826-.8587-.3826-.4983
 0-.7608.387t-.2625 1.01q0 .7208.3248 1.1123t.8586.3915q.436 0
 .7075-.3515.2714-.3514.2714-.9298m5.4706 2.2334q-.3737
 0-.5917-.2046t-.218-.5962v-1.9576q0-.2937-.0757-.5028-.0756-.2091-.2046-.3381a.81.81
 0 0 0-.3026-.1913 1.09 1.09 0 0 0-.3693-.0623q-.1424
 0-.2936.0578t-.2803.1913-.2091.347-.08.534v2.7228h-.3916q-.4272
 0-.6229-.2135-.1958-.2136-.1958-.5873v-5.606h.3738q.427 0
 .6362.2136t.2091.5517v1.3704q.0623-.1068.1735-.218a1.8 1.8 0 0 1
 .2447-.2047 1.4 1.4 0 0 1 .2937-.1557.9.9 0 0 1 .3292-.0623q.9344 0
 1.4504.5383.5161.5385.5161 1.5617v2.8118zm5.5595-2.5449q0 .5784-.1423
 1.0634-.1425.485-.4138.8409a1.85 1.85 0 0
 1-.6763.5516q-.4048.1959-.9298.1958-.4005
 0-.7164-.2002t-.4938-.5117v2.1178h-.3737a.87.87 0 0
 1-.3115-.0578.82.82 0 0 1-.267-.1646.83.83 0 0
 1-.1868-.258q-.0711-.1514-.0712-.3471v-2.9008q0-.5962.138-1.0945.1379-.4983.4315-.8543.2937-.356.7475-.5517t1.0856-.1957q.4805
 0
 .8809.2002.4004.2003.6896.5294.2892.3292.4494.7564.1602.427.1601.881m-1.228.3115q0-.8542-.2802-1.2369-.2803-.3826-.8587-.3826-.4983
 0-.7608.387t-.2625 1.01q0 .7208.3248 1.1123t.8587.3915q.4359 0
 .7074-.3515t.2714-.9298m6.0312.347q0
 .4627-.169.8186t-.4583.6007-.6674.3692-.7964.1246h-.6584q-1.6996
 0-1.6996-1.4504V8.6009q.1068-.0357.3025-.0846a8.5 8.5 0 0 1
 .4227-.0934 5.8 5.8 0 0 1
 .4627-.0712q.2357-.0267.4227-.0267h.7385q.436 0
 .8009.1112.3648.1113.6317.3204.267.209.4138.5072.1468.298.1468.6718 0
 .5072-.258.832t-.7119.4582q.2314.0624.4271.2047.1958.1425.3426.3248.1469.1824.227.396.08.2135.08.4093m-1.3258-2.5182q0-.1958-.0846-.3337a.64.64
 0 0 0-.218-.218q-.1335-.0801-.3025-.1157a1.64 1.64 0 0
 0-.3381-.0356h-.4538a1.7 1.7 0 0
 0-.2581.0223q-.1424.0222-.267.04v1.3792h.9344q.4093 0
 .6985-.1735t.2892-.565m.0979
 2.5538q0-.4983-.2536-.6852-.2536-.1868-.7875-.1868h-.97v1.2546q0
 .1602.1513.2714.1513.1113.3826.1112h.4983q.4984 0
 .7386-.209.2403-.2093.2403-.5562m6.04-.0356q0
 .4627-.169.8186t-.4583.6007-.6674.3692-.7964.1246h-.6585q-1.6995
 0-1.6995-1.4504V8.6009q.1068-.0357.3025-.0846a8.5 8.5 0 0 1
 .4227-.0934 5.8 5.8 0 0 1
 .4627-.0712q.2357-.0267.4226-.0267H21.9q.436 0
 .8009.1112.3648.1113.6317.3204.267.209.4138.5072.1468.298.1468.6718 0
 .5072-.258.832t-.7119.4582q.2313.0624.4271.2047a1.78 1.78 0 0 1
 .3426.3248q.1468.1824.227.396.08.2135.08.4093m-1.3258-2.5182q0-.1958-.0846-.3337a.64.64
 0 0 0-.218-.218q-.1335-.0801-.3025-.1157a1.64 1.64 0 0
 0-.3382-.0356h-.4538a1.7 1.7 0 0
 0-.258.0223q-.1425.0222-.267.04v1.3792h.9344q.4093 0
 .6985-.1735t.2892-.565m.0978
 2.5538q0-.4983-.2536-.6852-.2535-.1868-.7875-.1868h-.9699v1.2546q0
 .1602.1513.2714.1512.1113.3826.1112h.4983q.4983 0
 .7386-.209.2402-.2093.2402-.5562m.1952
 3.0812h-.1223v-.7305h.2823q.135 0 .2032.0494.0684.0494.0684.1605 0
 .099-.0558.1447-.0558.046-.1385.0547l.2086.3212h-.1384l-.1924-.3123h-.1151zm.1366-.4147a.8.8
 0 0 0 .0657-.0026.14.14 0 0 0 .0548-.015.1.1 0 0 0
 .0378-.0344q.0144-.022.0144-.0626 0-.0335-.0153-.053a.1.1 0 0
 0-.0387-.03.16.16 0 0 0-.0521-.0132.6.6 0 0
 0-.0558-.0026h-.1474v.2135zm.6546.037q0 .1484-.053.27a.63.63 0 0
 1-.1439.2083.65.65 0 0 1-.2104.134.67.67 0 0 1-.2509.0477q-.1455
 0-.267-.0503a.63.63 0 0 1-.2086-.1385.64.64 0 0 1-.1367-.209.69.69 0
 0 1-.0494-.2621q0-.1482.053-.27a.63.63 0 0 1 .1439-.2082.65.65 0 0 1
 .2113-.1341.68.68 0 0 1 .2535-.0477.67.67 0 0 1 .2509.0477.65.65 0 0
 1 .2104.134.63.63 0 0 1 .1439.2083q.053.1218.053.27m-.1439 0a.6.6 0 0
 0-.0395-.2205.52.52 0 0 0-.1097-.173.495.495 0 0 0-.1636-.112.51.51 0
 0 0-.2015-.0397.52.52 0 0 0-.204.0397.49.49 0 0 0-.1646.112.52.52 0 0
 0-.1097.173.6.6 0 0 0-.0395.2206q0 .113.036.2117a.52.52 0 0 0
 .1033.173.49.49 0 0 0 .1628.1173q.0952.0432.2158.0432a.51.51 0 0 0
 .2014-.0397.495.495 0 0 0 .1636-.112.52.52 0 0 0
 .1097-.172q.0396-.0997.0396-.2215" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
