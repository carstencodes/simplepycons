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


class YamlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yaml"

    @property
    def original_file_name(self) -> "str":
        return "yaml.svg"

    @property
    def title(self) -> "str":
        return "YAML"

    @property
    def primary_color(self) -> "str":
        return "#CB171E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YAML</title>
     <path d="m0 .97 4.111
 6.453v4.09h2.638v-4.09L11.053.969H8.214L5.58 5.125
 2.965.969Zm12.093.024-4.47 10.544h2.114l.97-2.345h4.775l.804
 2.345h2.26L14.255.994Zm1.133 2.225 1.463 3.87h-3.096zm3.06
 9.475v10.29H24v-2.199h-5.454v-8.091zm-12.175.002v10.335h2.217v-7.129l2.32
 4.792h1.746l2.4-4.96v7.295h2.127V12.696h-2.904L9.44
 17.37l-2.455-4.674Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Offic'''

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
