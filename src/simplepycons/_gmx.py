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


class GmxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gmx"

    @property
    def original_file_name(self) -> "str":
        return "gmx.svg"

    @property
    def title(self) -> "str":
        return "GMX"

    @property
    def primary_color(self) -> "str":
        return "#1C449B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GMX</title>
     <path d="M3.904 11.571v1.501H5.46c-.075.845-.712 1.274-1.539
 1.274-1.255 0-1.934-1.157-1.934-2.3 0-1.118.65-2.317 1.906-2.317.77 0
 1.321.468 1.586 1.166l1.812-.76C6.66 8.765 5.489 8.086 3.979 8.086
 1.614 8.087 0 9.654 0 12.037c0 2.309 1.604 3.876 3.913 3.876 1.227 0
 2.308-.439 3.025-1.44.651-.916.731-1.831.75-2.904zM13.65 8.3l-1.586
 3.95-1.5-3.95H8.67l-1.255 7.392h1.91l.619-4.257h.019l1.695
 4.257h.765l1.775-4.257h.024l.538 4.257h1.92L15.562 8.3zm7.708 3.473
 2.086-3.475h-2.128l-1.11 1.767L19.012 8.3H16.68l2.459 3.47-2.46
 3.922h2.333l1.33-2.223 1.576 2.223H24l-2.642-3.92" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.united-internet.de/en/newsroom/me'''

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
