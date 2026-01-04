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


class PlaneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plane"

    @property
    def original_file_name(self) -> "str":
        return "plane.svg"

    @property
    def title(self) -> "str":
        return "Plane"

    @property
    def primary_color(self) -> "str":
        return "#121212"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plane</title>
     <path d="M0 5.358a.854.854 0 0 1 1.235-.767L6.134 7.05v5.768c0
 .81.456 1.553 1.179 1.915l4.42 2.218v1.692a.853.853 0 0
 1-1.235.766L1.18 14.732A2.14 2.14 0 0 1 0 12.817zm6.134 0a.853.853 0
 0 1 1.235-.766l4.898 2.458v5.768c0 .81.457 1.552 1.18 1.915l4.42
 2.218v1.692a.853.853 0 0 1-1.235.765l-4.899-2.457v-5.769a2.14 2.14 0
 0 0-1.179-1.914L6.134 7.05zm6.133 0a.853.853 0 0 1 1.235-.766l9.319
 4.676A2.14 2.14 0 0 1 24 11.182v7.46a.853.853 0 0
 1-1.235.766l-4.899-2.457v-5.769a2.14 2.14 0 0
 0-1.179-1.914l-4.42-2.218z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://plane.so/brand-logos/logo-with-wordma'''

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
