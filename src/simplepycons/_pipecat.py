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


class PipecatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pipecat"

    @property
    def original_file_name(self) -> "str":
        return "pipecat.svg"

    @property
    def title(self) -> "str":
        return "Pipecat"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pipecat</title>
     <path d="M3.309 5.116a.87.87 0 0 1 .958.24L7.369
 8.89h9.262l3.102-3.536a.867.867 0 0 1
 1.52.573v7.807H24v1.735h-4.482V8.232l-1.842 2.099a.87.87 0 0
 1-.652.295H6.976a.87.87 0 0
 1-.652-.295l-1.842-2.1v7.239H0v-1.735h2.747V5.928c0-.362.224-.685.562-.812m16.209
 12.089H24v1.735h-4.482zM0 17.205h4.482v1.735H0zm9.253-2.892a1.157
 1.157 0 1 1-2.314 0 1.157 1.157 0 0 1 2.314 0m7.807 0a1.157 1.157 0 1
 1-2.313 0 1.157 1.157 0 0 1 2.313 0" />
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
