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


class RevealdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "revealdotjs"

    @property
    def original_file_name(self) -> "str":
        return "revealdotjs.svg"

    @property
    def title(self) -> "str":
        return "reveal.js"

    @property
    def primary_color(self) -> "str":
        return "#F2E142"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>reveal.js</title>
     <path d="M4.271 1.352a.774.774 0 0 0-.787.775v19.761c0
 .49.45.857.93.758l6.676-1.382-2.77-.614-3.675.762V2.607l3.101.686
 2.777-.574-6.097-1.35a.774.774 0 0 0-.155-.017zm15.315.002L5.145
 4.344v15.092l14.43 3.195a.774.774 0 0 0 .94-.758V2.111a.773.773 0 0
 0-.93-.757zM2.984 4.79l-2.367.49A.774.774 0 0 0 0
 6.04v11.639a.774.774 0 0 0
 .607.754l2.377.525V4.791zm18.034.252V6.23l1.822.405v11.011l-1.822.377v1.186l2.365-.49A.774.774
 0 0 0 24 17.96V6.322a.774.774 0 0 0-.607-.754l-2.375-.525z" />
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
