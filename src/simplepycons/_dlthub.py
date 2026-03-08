#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class DlthubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dlthub"

    @property
    def original_file_name(self) -> "str":
        return "dlthub.svg"

    @property
    def title(self) -> "str":
        return "dlthub"

    @property
    def primary_color(self) -> "str":
        return "#59C1D5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>dlthub</title>
     <path d="M24 11.498h-1.008v3.01H24Zm-3.024
 0h2.016v-1.004h-2.016V8.487h-1.008v7.025h3.024v-1.004h-2.016zm-2.986
 3.01h-2.016v1.004h3.024v-5.017H17.99zm-2.016-4.013h-1.008v4.014h1.008zm-2.985
 1.003h-2.016v-3.01H9.965v7.024h1.008v-3.01h2.016v3.01h1.008V8.488h-1.008zm-11.981
 0H0v3.01h1.008zm2.016-1.003H1.008v1.003h2.016v3.01H1.008v1.004h3.024V8.488H3.024zM5
 15.512h1.01V8.488H5.001Zm2.986-7.024H6.98v6.02h1.008v-3.01h1.008v-1.003H7.987zm1.008
 6.02H7.987v1.004h1.008z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dlt-hub/dlt/blob/3201e053d'''

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
