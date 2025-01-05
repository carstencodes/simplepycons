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


class AbstractIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "abstract"

    @property
    def original_file_name(self) -> "str":
        return "abstract.svg"

    @property
    def title(self) -> "str":
        return "Abstract"

    @property
    def primary_color(self) -> "str":
        return "#191A1B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Abstract</title>
     <path d="M12 0c9.601 0 12 2.399 12 12 0 9.601-2.399 12-12
 12-9.601 0-12-2.399-12-12C0 2.399 2.399 0 12 0zm-1.969
 18.564c2.524.003 4.604-2.07 4.609-4.595
 0-2.521-2.074-4.595-4.595-4.595S5.45 11.449 5.45 13.969c0 2.516 2.065
 4.588 4.581
 4.595zm8.344-.189V5.625H5.625v2.247h10.498v10.503h2.252zm-8.344-6.748a2.343
 2.343 0 11-.002 4.686 2.343 2.343 0 01.002-4.686z" />
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
