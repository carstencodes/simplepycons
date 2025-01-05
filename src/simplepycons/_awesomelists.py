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


class AwesomeListsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "awesomelists"

    @property
    def original_file_name(self) -> "str":
        return "awesomelists.svg"

    @property
    def title(self) -> "str":
        return "Awesome Lists"

    @property
    def primary_color(self) -> "str":
        return "#FC60A8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Awesome Lists</title>
     <path d="M24 11.438l-6.154-5.645-.865.944 5.128
 4.7H1.895l5.128-4.705-.865-.943-6.154 5.649H0v3.72c0 1.683 1.62 3.053
 3.61 3.053h3.795c1.99 0 3.61-1.37 3.61-3.051v-2.446h1.97v2.446c0 1.68
 1.62 3.051 3.61 3.051h3.794c1.99 0 3.61-1.37 3.61-3.051v-3.721z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sindresorhus/awesome/tree/'''

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
