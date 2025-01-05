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


class UmlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uml"

    @property
    def original_file_name(self) -> "str":
        return "uml.svg"

    @property
    def title(self) -> "str":
        return "UML"

    @property
    def primary_color(self) -> "str":
        return "#FABD14"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UML</title>
     <path d="M10.768 0 7.182 1.604s6.126 2.72 6.852 3.055c.72.335
 1.744.947.565
 1.629-1.18.682-2.423.477-3.259.09-.835-.384-7.012-3.257-7.012-3.257L.666
 4.777s6.4 2.935 7.4 3.417c1.003.482 4.753 1.784 8.48.002 3.727-1.781
 3.261-2.577
 3.268-2.724.006-.148-.036-.933-.632-1.467-.599-.534-2.378-1.375-3.127-1.73C15.305
 1.916 10.77 0 10.77 0ZM.411 5.299v13.215l2.904 1.402v-7.963l1.585 8.6
 2.58 1.243 1.66-7.154v7.826l2.916 1.38V10.643L7.629 8.628l-1.403
 6.296-1.412-7.598Zm16.76 3.115-4.624 2.315L12.559
 24l11.03-5.225-.025-3.613-6.393 2.92Z" />
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
        yield from [
            "Unified Modelling Language",
        ]
