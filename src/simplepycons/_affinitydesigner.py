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


class AffinityDesignerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "affinitydesigner"

    @property
    def original_file_name(self) -> "str":
        return "affinitydesigner.svg"

    @property
    def title(self) -> "str":
        return "Affinity Designer"

    @property
    def primary_color(self) -> "str":
        return "#134881"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Affinity Designer</title>
     <path d="M24 2.344v19.312A2.345 2.345 0 0 1 21.656 24H2.344A2.345
 2.345 0 0 1 0 21.656V2.344A2.345 2.345 0 0 1 2.344 0h19.312A2.345
 2.345 0 0 1 24 2.344ZM1.758 21.305c0
 .517.42.937.938.937h8.226l-4.299-7.445 7.528-13.039h-3.482L1.758
 17.192v4.113Zm11.418-6.866-2.712-4.698-1.761 3.051a1.098 1.098 0 0 0
 .952 1.647h3.521Zm9.066 6.873v-6.075H7.799l4.044 7.005h9.462a.937.937
 0 0 0 .937-.93Zm-.937-19.554h-6.232l-4.148 7.185 3.173
 5.496h8.144V2.688a.937.937 0 0 0-.937-.93Z" />
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
