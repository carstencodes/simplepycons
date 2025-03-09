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


class XyflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xyflow"

    @property
    def original_file_name(self) -> "str":
        return "xyflow.svg"

    @property
    def title(self) -> "str":
        return "xyflow"

    @property
    def primary_color(self) -> "str":
        return "#1A192B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>xyflow</title>
     <path d="M2 0a2 2 0 0 0-2 2v6.667a2 2 0 0 0 2 2h6.667a2 2 0 0 0
 2-2V7.22a2 2 0 0 1-1.334 0v1.447a.667.667 0 0 1-.666.666H2a.667.667 0
 0 1-.667-.666V2c0-.368.299-.667.667-.667h6.667c.368 0
 .666.299.666.667v1.447a2 2 0 0 1 1.334 0V2a2 2 0 0 0-2-2zm11.333 2a2
 2 0 0 1 2-2H22a2 2 0 0 1 2 2v6.667a2 2 0 0 1-2 2h-1.447a2 2 0 0 0
 0-1.334H22a.667.667 0 0 0 .667-.666V2A.667.667 0 0 0 22
 1.333h-6.667a.667.667 0 0 0-.666.667v1.447a2 2 0 0 0-1.334 0zm3.448
 7.333h-1.448a.667.667 0 0 1-.666-.666V7.22a2 2 0 0 1-1.334 0v1.447a2
 2 0 0 0 2 2h1.447a2 2 0 0 1 0-1.334M0 15.333a2 2 0 0 1 2-2h6.667a2 2
 0 0 1 2 2v1.447a2 2 0 0 0-1.334 0v-1.447a.667.667 0 0
 0-.666-.666H2a.667.667 0 0 0-.667.666V22c0
 .368.299.667.667.667h6.667A.667.667 0 0 0 9.333 22v-1.447a2 2 0 0 0
 1.334 0V22a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm22-.666h-1.447a2 2 0 0 0
 0-1.334H22a2 2 0 0 1 2 2V22a2 2 0 0 1-2 2h-6.667a2 2 0 0
 1-2-2v-1.447a2 2 0 0 0 1.334 0V22c0 .368.298.667.666.667H22a.667.667
 0 0 0 .667-.667v-6.667a.667.667 0 0 0-.667-.666m-7.333
 2.114v-1.448c0-.368.298-.666.666-.666h1.447a2 2 0 0 1
 0-1.334h-1.447a2 2 0 0 0-2 2v1.447a2 2 0 0 1 1.334 0M20 14a1.333
 1.333 0 1 1-1.667-1.291V11.29a1.334 1.334 0 1 1 .667 0v1.418c.575.148
 1 .67 1 1.291m-10 6c.621 0 1.143-.425 1.291-1h1.418a1.334 1.334 0 1 0
 0-.667H11.29A1.334 1.334 0 1 0 10 20m1.291-14.333a1.334 1.334 0 1 1
 0-.667h1.418a1.334 1.334 0 1 1 0 .667z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/xyflow/web/blob/fe6af5d1c7'''

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
        yield from [
            "reactflow",
            "svelteflow",
        ]
