#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class OxcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oxc"

    @property
    def original_file_name(self) -> "str":
        return "oxc.svg"

    @property
    def title(self) -> "str":
        return "Oxc"

    @property
    def primary_color(self) -> "str":
        return "#00F7F1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Oxc</title>
     <path d="M15.463 3.923c0 .637.517 1.154 1.154 1.154h4.376c.515 0
 .772.62.408.984l-5.6 5.601c-.217.216-.34.51-.34.816v1.915c0 .797.79
 1.35 1.49.97.71-.386 1.371-.853 1.972-1.392a.603.603 0 0 1
 .828.012l4.08 4.08a.56.56 0 0 1-.007.808A17.25 17.25 0 0 1 12 23.54
 17.25 17.25 0 0 1 .176 18.872a.56.56 0 0
 1-.006-.81l4.08-4.078a.604.604 0 0 1 .827-.012 10.4 10.4 0 0 0 1.973
 1.39c.7.38 1.488-.171 1.488-.968v-1.915c0-.307-.122-.6-.339-.816L2.6
 6.061a.576.576 0 0 1 .408-.984h4.376c.637 0 1.154-.517
 1.154-1.154V1.038c0-.32.258-.577.577-.577h5.77c.318 0
 .576.258.576.577v2.885z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/voidzero-dev/community-des
ign-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-asse'''

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
