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


class DialogflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dialogflow"

    @property
    def original_file_name(self) -> "str":
        return "dialogflow.svg"

    @property
    def title(self) -> "str":
        return "Dialogflow"

    @property
    def primary_color(self) -> "str":
        return "#FF9800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dialogflow</title>
     <path d="M11.996 0a1.639 1.639 0 0 0-.82.22L3.344 4.74a1.648
 1.648 0 0 0-.535.498l9.136 5.28 9.213-5.32a1.652 1.652 0 0
 0-.51-.458L12.818.22a1.639 1.639 0 0 0-.822-.22zm9.336 5.5l-9.387
 5.422-9.3-5.373a1.648 1.648 0 0 0-.12.615v9.043a1.643 1.643 0 0 0
 .819 1.42l3.918 2.266v4.617a.493.493 0 0 0 .74.424l12.654-7.303a1.639
 1.639 0 0 0 .819-1.42V6.162a1.652 1.652 0 0 0-.143-.662z" />
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
