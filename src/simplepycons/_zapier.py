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


class ZapierIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zapier"

    @property
    def original_file_name(self) -> "str":
        return "zapier.svg"

    @property
    def title(self) -> "str":
        return "Zapier"

    @property
    def primary_color(self) -> "str":
        return "#FF4F00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zapier</title>
     <path d="M4.157 0A4.151 4.151 0 0 0 0 4.161v15.678A4.151 4.151 0
 0 0 4.157 24h15.682A4.152 4.152 0 0 0 24 19.839V4.161A4.152 4.152 0 0
 0 19.839 0H4.157Zm10.61 8.761h.03a.577.577 0 0 1 .23.038.585.585 0 0
 1 .201.124.63.63 0 0 1 .162.431.612.612 0 0 1-.162.435.58.58 0 0
 1-.201.128.58.58 0 0 1-.23.042.529.529 0 0 1-.235-.042.585.585 0 0
 1-.332-.328.559.559 0 0 1-.038-.235.613.613 0 0 1 .17-.431.59.59 0 0
 1 .405-.162Zm2.853
 1.572c.03.004.061.004.095.004.325-.011.646.064.937.219.238.144.431.355.552.609.128.279.189.582.185.888v.193a2
 2 0 0 1 0 .219h-2.498c.003.227.075.45.204.642a.78.78 0 0 0
 .646.265.714.714 0 0 0 .484-.136.642.642 0 0 0
 .23-.318l.915.257a1.398 1.398 0 0
 1-.28.537c-.14.159-.321.284-.521.355a2.234 2.234 0 0 1-.836.136 1.923
 1.923 0 0 1-1.001-.245 1.618 1.618 0 0 1-.665-.703 2.221 2.221 0 0
 1-.227-1.036 1.95 1.95 0 0 1 .48-1.398 1.9 1.9 0 0 1
 1.3-.488Zm-9.607.023c.162.004.325.026.48.079.207.065.4.174.563.314.26.302.393.692.366
 1.088v2.276H8.53l-.109-.711h-.065c-.064.163-.155.31-.272.439a1.122
 1.122 0 0 1-.374.264 1.023 1.023 0 0 1-.453.083 1.334 1.334 0 0
 1-.866-.264.965.965 0 0 1-.329-.801.993.993 0 0 1 .076-.431 1.02 1.02
 0 0 1 .242-.363 1.478 1.478 0 0 1 1.043-.303h.952v-.181a.696.696 0 0
 0-.136-.454.553.553 0 0 0-.438-.154.695.695 0 0 0-.378.086.48.48 0 0
 0-.193.254l-.99-.144a1.26 1.26 0 0 1
 .257-.563c.14-.174.321-.302.533-.378.261-.091.54-.136.82-.129.053-.003.106-.007.163-.007Zm4.384.007c.174
 0 .347.038.506.114.182.083.34.211.458.374.257.423.377.911.351
 1.406a2.53 2.53 0 0 1-.355 1.448 1.148 1.148 0 0 1-1.009.517c-.204
 0-.401-.045-.582-.136a1.052 1.052 0 0 1-.48-.457 1.298 1.298 0 0
 1-.114-.234h-.045l.004
 1.784h-1.059v-4.713h.904l.117.805h.057c.068-.208.177-.401.328-.56a1.129
 1.129 0 0 1 .843-.344h.076v-.004Zm7.559.084h.903l.113.805h.053a1.37
 1.37 0 0 1 .235-.484.813.813 0 0 1 .313-.242.82.82 0 0 1
 .39-.076h.234v1.051h-.401a.662.662 0 0 0-.313.008.623.623 0 0
 0-.272.155.663.663 0 0 0-.174.26.683.683 0 0
 0-.027.314v1.875h-1.054v-3.666Zm-17.515.003h3.262v.896L3.73
 13.104l.034.113h1.973l.042.9H2.4v-.9l1.931-1.754-.045-.117H2.441v-.896Zm11.815
 0h1.055v3.659h-1.055V10.45Zm3.443.684.019.016a.69.69 0 0
 0-.351.045.756.756 0 0
 0-.287.204c-.11.155-.174.336-.189.522h1.545c-.034-.526-.257-.787-.74-.787h.003Zm-5.718.163c-.026
 0-.057 0-.083.004a.78.78 0 0 0-.31.053.746.746 0 0 0-.257.189 1.016
 1.016 0 0 0-.204.695v.064c-.015.257.057.507.204.711a.634.634 0 0 0
 .253.196.638.638 0 0 0 .314.061.644.644 0 0 0
 .578-.265c.14-.223.204-.48.189-.74a1.216 1.216 0 0
 0-.181-.711.677.677 0 0 0-.503-.257Zm-4.509 1.266a.464.464 0 0
 0-.268.102.373.373 0 0 0-.114.276c0 .053.008.106.027.155a.375.375 0 0
 0 .087.132.576.576 0 0 0 .397.11v.004a.863.863 0 0 0
 .563-.182.573.573 0 0 0 .211-.457v-.14h-.903Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.figma.com/file/NQFxTCE5pGR3dHZt0D
kOyy/Zapier-Brand-Guidelines-%5BExternal%5D?type=design&node-id=101-97'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.figma.com/file/NQFxTCE5pGR3dHZt0D
kOyy/Zapier-Brand-Guidelines-%5BExternal%5D?type=design&node-id=101-97'''

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
