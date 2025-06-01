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


class VoelknerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "voelkner"

    @property
    def original_file_name(self) -> "str":
        return "voelkner.svg"

    @property
    def title(self) -> "str":
        return "voelkner"

    @property
    def primary_color(self) -> "str":
        return "#94C125"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>voelkner</title>
     <path d="M19.4 3.502C18.093 8.84 15.018 16.05 11.964 16.05S5.841
 8.827 4.552 3.502H0c.229 1.007 1.121 4.707 2.597 8.122 2.543 5.89
 5.695 8.876 9.367 8.876s6.828-2.991 9.385-8.893C22.806 8.247 23.737
 4.592 24 3.5h-4.6z" />
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
