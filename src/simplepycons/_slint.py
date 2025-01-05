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


class SlintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "slint"

    @property
    def original_file_name(self) -> "str":
        return "slint.svg"

    @property
    def title(self) -> "str":
        return "Slint"

    @property
    def primary_color(self) -> "str":
        return "#2379F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Slint</title>
     <path d="m6.503 23.914
 13.61-9.399s.614-.351.614-.906c0-.739-.776-.979-.776-.979l-7.488-2.953c-.267-.104-.634.189-.29.56l2.479
 2.471s.688.675.688 1.117-.423.836-.423.836l-9.02
 8.684c-.32.31.113.87.606.569zM17.497.087 3.887
 9.484s-.614.351-.614.906c0 .739.776.98.776.98l7.488
 2.953c.267.103.636-.19.29-.559l-2.479-2.48s-.688-.673-.688-1.116c0-.444.423-.837.423-.837L18.097.654c.326-.31-.106-.87-.6-.567z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/slint-ui/slint/blob/master'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/slint-ui/slint/blob/10ae5c'''

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
