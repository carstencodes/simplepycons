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


class KnimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "knime"

    @property
    def original_file_name(self) -> "str":
        return "knime.svg"

    @property
    def title(self) -> "str":
        return "KNIME"

    @property
    def primary_color(self) -> "str":
        return "#FDD800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KNIME</title>
     <path d="m10.445 21.393 11.54-.775.451.775zM7.56 11.113l-5.092
 10.28h-.904Zm10.427 2.652-6.43-9.505.452-.775zm2.57
 5.216.627.896-10.652.707zM4.655 20.976l-1.143.09
 4.709-9.488Zm6.173-14.667.476-.998 5.984 8.782zm8.272 11.055.847
 1.015-8.685 1.413zM6.76 20.532l-1.32.224
 3.11-8.162Zm3.406-12.189.472-1.207 5.558 6.732Zm7.403 7.54 1.13
 1.016-6.378 1.98zm-8.759 4.08-1.46.448 1.46-6.44zm.8-9.539.363-1.48
 4.868 4.477zm-.348 9.402v-7.851l.244-1.085 6.864 3.926.834.758L10.34
 19.5zM12.01 1.694 0 22.306h24z" />
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
