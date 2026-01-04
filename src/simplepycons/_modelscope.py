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


class ModelscopeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "modelscope"

    @property
    def original_file_name(self) -> "str":
        return "modelscope.svg"

    @property
    def title(self) -> "str":
        return "ModelScope"

    @property
    def primary_color(self) -> "str":
        return "#624AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ModelScope</title>
     <path d="M2.667
 5.333V8H0v5.333h2.667v-2.666H.5V8.5h2.166v2.166h2.666V8H8V5.333Zm0
 8v5.334H8V16H5.333v-2.667Zm13.333-8V8h2.667v2.667h2.666V8.5H23.5v2.166h-2.166v2.666H24V8h-2.667V5.333Zm5.333
 8h-2.666V16H16v2.667h5.333zM8 10.667v2.666h2.667v-2.666zm2.667
 2.666V16h2.666v-2.667zm2.666 0H16v-2.666h-2.667z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://modelscope.cn/models/modelscope/logos'''

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
