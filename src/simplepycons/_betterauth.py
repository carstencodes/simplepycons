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


class BetterAuthIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "betterauth"

    @property
    def original_file_name(self) -> "str":
        return "betterauth.svg"

    @property
    def title(self) -> "str":
        return "Better Auth"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Better Auth</title>
     <path d="M0 3.39v17.22h5.783V15.06h6.434V8.939H5.783V3.39ZM12.217
 8.94h5.638v6.122h-5.638v5.548H24V3.391H12.217Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/better-auth/better-auth/bl
ob/fd62eba1d0ec71b3abb17ece92a4aae0c3c85270/docs/public/branding/bette'''

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
