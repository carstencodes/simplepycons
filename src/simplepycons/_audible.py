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


class AudibleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "audible"

    @property
    def original_file_name(self) -> "str":
        return "audible.svg"

    @property
    def title(self) -> "str":
        return "Audible"

    @property
    def primary_color(self) -> "str":
        return "#F8991C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Audible</title>
     <path d="M12.008 17.362L24 9.885v2.028l-11.992 7.509L0
 11.912V9.886l12.008 7.477zm0-9.378c-2.709 0-5.085 1.363-6.448
 3.47.111-.111.175-.175.286-.254 3.374-2.804 8.237-2.17 10.883
 1.362l1.758-1.124c-1.394-2.044-3.786-3.454-6.48-3.454m0 3.47a4.392
 4.392 0 0 0-3.548 1.821 3.597 3.597 0 0 1 2.139-.697c1.299 0
 2.455.666 3.232
 1.79l1.679-1.045c-.729-1.157-2.028-1.87-3.501-1.87M3.897
 8.412c4.943-3.897 11.929-2.836 15.652 2.344l.031.032
 1.822-1.125a11.214 11.214 0 0 0-9.394-5.085c-3.897 0-7.366
 1.996-9.394 5.085.364-.412.824-.903 1.283-1.251" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Audib'''

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
