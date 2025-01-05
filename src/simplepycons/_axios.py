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


class AxiosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "axios"

    @property
    def original_file_name(self) -> "str":
        return "axios.svg"

    @property
    def title(self) -> "str":
        return "Axios"

    @property
    def primary_color(self) -> "str":
        return "#5A29E4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Axios</title>
     <path d="M11.0683 2.89968V22.2973l-2.11399
 1.70265V7.8638H4.975l6.0933-4.96412zM14.93426
 0v15.76724H19.025l-6.20044 5.08865V1.4689L14.93426 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/axios/axios-docs/blob/ba35'''

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
