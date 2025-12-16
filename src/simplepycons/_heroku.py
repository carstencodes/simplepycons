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


class HerokuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "heroku"

    @property
    def original_file_name(self) -> "str":
        return "heroku.svg"

    @property
    def title(self) -> "str":
        return "Heroku"

    @property
    def primary_color(self) -> "str":
        return "#430098"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Heroku</title>
     <path d="M20.61 0H3.39C2.189 0 1.23.96 1.23 2.16v19.681c0
 1.198.959 2.159 2.16 2.159h17.22c1.2 0 2.159-.961
 2.159-2.159V2.16C22.77.96 21.811 0 20.61 0zm.96 21.841c0
 .539-.421.96-.96.96H3.39c-.54
 0-.96-.421-.96-.96V2.16c0-.54.42-.961.96-.961h17.22c.539 0
 .96.421.96.961v19.681zM6.63 20.399L9.33
 18l-2.7-2.4v4.799zm9.72-9.719c-.479-.48-1.379-1.08-2.879-1.08-1.621
 0-3.301.421-4.5.84V3.6h-2.4v10.38l1.68-.78s2.76-1.26 5.16-1.26c1.2 0
 1.5.66 1.5 1.26v7.2h2.4v-7.2c.059-.179.059-1.501-.961-2.52zM13.17
 7.5h2.4c1.08-1.26 1.62-2.521 1.8-3.9h-2.399c-.241 1.379-.841
 2.64-1.801 3.9z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://devcenter.heroku.com/articles/heroku-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://devcenter.heroku.com/articles/heroku-'''

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
