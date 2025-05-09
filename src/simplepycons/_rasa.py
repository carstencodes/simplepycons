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


class RasaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rasa"

    @property
    def original_file_name(self) -> "str":
        return "rasa.svg"

    @property
    def title(self) -> "str":
        return "Rasa"

    @property
    def primary_color(self) -> "str":
        return "#5A17EE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rasa</title>
     <path d="m20.848
 15.852-3.882-2.034H.97V7.515h22.06v6.303h-2.182v2.034ZM0
 6.545v8.243h16.727l5.091 2.667v-2.667H24V6.545H0Zm1.94
 1.94h4.12v2.18l-1.33.517 1.362
 1.666H4.84l-1.06-1.296-.87.339v.957h-.97V8.485ZM8
 12.848h-.97V8.485h4.364v4.363h-.97v-1.454H8v1.454Zm4.364-1.696V8.485h4.363v.97h-3.394v.727h3.394v2.666h-4.363v-.97h3.394v-.726h-3.394Zm5.333-.243V8.485h4.364v4.363h-.97v-1.454h-2.424v1.454h-.97V10.91Zm-14.788-.06
 2.182-.848v-.546H2.909v1.395ZM8
 9.456v.97h2.424v-.97H8Zm13.09.97v-.97h-2.423v.97h2.424Z" />
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
