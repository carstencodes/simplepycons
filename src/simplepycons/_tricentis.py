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


class TricentisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tricentis"

    @property
    def original_file_name(self) -> "str":
        return "tricentis.svg"

    @property
    def title(self) -> "str":
        return "Tricentis"

    @property
    def primary_color(self) -> "str":
        return "#12438C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tricentis</title>
     <path d="M14.271 10.42 6.86 3.006 9.833.034l4.438 4.438L18.742
 0l2.974 2.974ZM9.825 24l-2.973-2.974 7.445-7.445 7.412 7.412-2.974
 2.973-4.438-4.437zm-4.567-4.568-2.974-2.974 4.47-4.47-4.437-4.439
 2.974-2.974 7.412 7.412Z" />
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
