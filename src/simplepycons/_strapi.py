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


class StrapiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "strapi"

    @property
    def original_file_name(self) -> "str":
        return "strapi.svg"

    @property
    def title(self) -> "str":
        return "Strapi"

    @property
    def primary_color(self) -> "str":
        return "#4945FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Strapi</title>
     <path d="M8.32 0c-3.922 0-5.882 0-7.1 1.219C0 2.438 0 4.399 0
 8.32v7.36c0 3.922 0 5.882 1.219 7.101C2.438 24 4.399 24 8.32
 24h7.36c3.922 0 5.882 0 7.101-1.219C24 21.562 24 19.601 24
 15.68V8.32c0-3.922 0-5.882-1.219-7.101C21.562 0 19.601 0 15.68
 0H8.32zm.41 7.28h7.83a.16.16 0 0 1 .16.16v7.83h-3.87v-3.71a.41.41 0 0
 0-.313-.398l-.086-.012h-3.72V7.28zm-.5.25v3.87H4.553a.08.08 0 0
 1-.057-.136L8.23 7.529zm.25 4.12h3.87v3.87H8.64a.16.16 0 0
 1-.16-.16v-3.71zm4.12 4.12h3.87l-3.734 3.734a.08.08 0 0
 1-.136-.057V15.77z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://handbook.strapi.io/strapi-brand-book-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://handbook.strapi.io/strapi-brand-book-'''

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
