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


class WebgpuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webgpu"

    @property
    def original_file_name(self) -> "str":
        return "webgpu.svg"

    @property
    def title(self) -> "str":
        return "WebGPU"

    @property
    def primary_color(self) -> "str":
        return "#005A9C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WebGPU</title>
     <path d="m0 4.784 8.652 14.432 8.652-14.432zm22.032.145L20.07
 8.202H24L22.032 4.93zm-4.46 0-4.192 6.993h8.384zm2.498 3.575 1.962
 3.273L24 8.504zm-6.69 3.72 4.192 6.992 4.192-6.992z" />
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
