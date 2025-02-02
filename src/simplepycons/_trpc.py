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


class TrpcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trpc"

    @property
    def original_file_name(self) -> "str":
        return "trpc.svg"

    @property
    def title(self) -> "str":
        return "tRPC"

    @property
    def primary_color(self) -> "str":
        return "#2596BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>tRPC</title>
     <path d="M24 12c0 6.62-5.38 12-12 12S0 18.62 0 12 5.38 0 12 0s12
 5.38 12 12ZM1.21 12A10.78 10.78 0 0 0 12 22.79 10.78 10.78 0 0 0
 22.79 12 10.78 10.78 0 0 0 12 1.21 10.78 10.78 0 0 0 1.21
 12Zm10.915-6.086 2.162 1.248a.25.25 0 0 1 .125.217v1.103l2.473
 1.428a.25.25 0 0 1 .125.217v2.355l.955.551a.25.25 0 0 1
 .125.217v2.496a.25.25 0 0 1-.125.217l-2.162 1.248a.25.25 0 0 1-.25
 0l-.956-.552-2.472 1.427a.25.25 0 0 1-.25
 0l-2.472-1.427-.956.552a.25.25 0 0 1-.25 0l-2.162-1.248a.25.25 0 0
 1-.125-.217V13.25a.25.25 0 0 1 .125-.217l.955-.551v-2.355a.25.25 0 0
 1 .125-.217l2.473-1.428V7.38a.25.25 0 0 1
 .125-.217l2.162-1.248a.25.25 0 0 1 .25 0Zm1.268 10.049a.25.25 0 0
 1-.125-.217V13.25a.25.25 0 0 1 .125-.217l2.16-1.248a.25.25 0 0 1 .25
 0l.707.408v-1.922l-2.098-1.21v.814a.25.25 0 0 1-.125.217l-2.162
 1.248a.25.25 0 0 1-.25 0l-2.162-1.248a.25.25 0 0
 1-.125-.217V9.06L7.49 10.271v1.922l.707-.408a.25.25 0 0 1 .25 0l2.16
 1.248a.25.25 0 0 1 .125.217v2.496a.25.25 0 0 1-.125.217l-.705.408L12
 17.582l2.098-1.211ZM10.088 9.73l1.662.96V8.766l-1.662-.955Zm3.824
 0V7.811l-1.662.955v1.924ZM12 6.418l-1.66.96 1.66.954 1.66-.954Zm-5.59
 9.184 1.66.958v-1.921l-1.66-.956Zm3.822
 0v-1.92l-1.662.957v1.923Zm-1.91-3.311-1.662.96 1.661.955
 1.66-.956Zm5.446 3.31 1.66.96v-1.922l-1.66-.956Zm3.822
 0v-1.918l-1.662.956v1.922Zm-1.912-3.31-1.66.96 1.66.955 1.66-.956Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/trpc/trpc/blob/e0df4a2d5b4'''

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
