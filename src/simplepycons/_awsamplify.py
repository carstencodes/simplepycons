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


class AwsAmplifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "awsamplify"

    @property
    def original_file_name(self) -> "str":
        return "awsamplify.svg"

    @property
    def title(self) -> "str":
        return "AWS Amplify"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AWS Amplify</title>
     <path d="M5.223 17.905h6.76l1.731 3.047H0l4.815-8.344 2.018-3.494
 1.733 3.002zm2.52-10.371L9.408 4.65l9.415
 16.301h-3.334zm2.59-4.486h3.33L24 20.952h-3.334z" />
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
