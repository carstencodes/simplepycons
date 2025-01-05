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


class DictionarydotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dictionarydotcom"

    @property
    def original_file_name(self) -> "str":
        return "dictionarydotcom.svg"

    @property
    def title(self) -> "str":
        return "Dictionary.com"

    @property
    def primary_color(self) -> "str":
        return "#0049D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dictionary.com</title>
     <path d="M11.894.087 1.043 0a.3.3 0 0 0-.305.293V18.97a.331.331 0
 0 0 .166.28l8.13 4.713a.268.268 0 0 0 .364-.092.27.27 0 0 0
 .038-.138V6.275a.33.33 0 0 0-.176-.292L4.944 3.625a.173.173 0 0
 1-.084-.21.173.173 0 0 1 .197-.112l7.804 1.333a.31.31 0 0 1
 .252.302v15.717a.307.307 0 0 0 .309.308h.035c5.781-.645 9.72-4.693
 9.804-10.308.078-6.28-4.595-10.48-11.367-10.568Z" />
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
