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


class FacepunchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "facepunch"

    @property
    def original_file_name(self) -> "str":
        return "facepunch.svg"

    @property
    def title(self) -> "str":
        return "Facepunch"

    @property
    def primary_color(self) -> "str":
        return "#EC1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Facepunch</title>
     <path d="M12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.388
 12-12S18.629 0 12 0zm0 21.314c-5.133 0-9.297-4.164-9.297-9.297S6.867
 2.72 12 2.72s9.297 4.164 9.297 9.297-4.164 9.297-9.297 9.297zM10.028
 12l1.48 1.479-1.922 1.92-1.478-1.478-1.428 1.444-1.92-1.92L6.203
 12l-1.377-1.377 1.92-1.904 1.36 1.377 1.411-1.41 1.921 1.903L10.03
 12zm9.162-1.462-1.411 1.411 1.479 1.479-1.92 1.904-1.48-1.48-1.444
 1.446-1.904-1.921 1.445-1.428-1.377-1.377 1.904-1.92 1.376 1.376
 1.411-1.41 1.92 1.92z" />
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
