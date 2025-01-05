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


class AuthentikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "authentik"

    @property
    def original_file_name(self) -> "str":
        return "authentik.svg"

    @property
    def title(self) -> "str":
        return "Authentik"

    @property
    def primary_color(self) -> "str":
        return "#FD4B2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Authentik</title>
     <path d="M13.96
 9.01h-.84V7.492h-1.234v3.663H5.722c.34.517.538.982.538 1.152 0
 .46-1.445 3.059-3.197 3.059C.8 15.427-.745 12.8.372 10.855a3.062
 3.062 0 0 1 2.691-1.606c1.04 0 1.971.915 2.557 1.755V6.577a3.773
 3.773 0 0 1 3.77-3.769h10.84C22.31 2.808 24 4.5 24 6.577v10.845a3.773
 3.773 0 0 1-3.77 3.769h-1.6V17.5h-7.64v3.692h-1.6a3.773 3.773 0 0
 1-3.77-3.769v-3.41h12.114v-6.52h-1.59v.893h-.84v-.893H13.96v1.516Zm-9.956
 1.845c-.662-.703-1.578-.544-2.209 0-2.105 2.054 1.338 5.553 3.302
 1.447a5.395 5.395 0 0 0-1.093-1.447Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/goauthentik/authentik/blob'''

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
