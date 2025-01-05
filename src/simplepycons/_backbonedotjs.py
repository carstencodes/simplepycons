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


class BackbonedotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "backbonedotjs"

    @property
    def original_file_name(self) -> "str":
        return "backbonedotjs.svg"

    @property
    def title(self) -> "str":
        return "Backbone.js"

    @property
    def primary_color(self) -> "str":
        return "#0071B5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Backbone.js</title>
     <path d="M2.34 0v10.45l3.2-1.83V5.27l2.93 1.67 3.01-1.72L2.34
 0zm19.31 0L12.5 5.22l3.02 1.73 2.94-1.68v3.35l3.2 1.83V0h-.01zm-9.9
 5.64-9.4 5.38V24l9.4-5.36v-3.76l-6.21 3.56v-5.5l6.21-3.54V5.64zm.5
 0V9.4l6.22 3.54v5.5l-6.22-3.56v3.76L21.66 24V11.02l-9.41-5.38zM7.7
 12.3l-1.65.94v1.86l2.17 1.24 3.28-1.87-3.8-2.17zm8.61 0-3.8 2.16 3.28
 1.88 2.17-1.24v-1.86l-1.65-.94z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Backb'''

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
