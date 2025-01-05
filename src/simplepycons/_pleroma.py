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


class PleromaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pleroma"

    @property
    def original_file_name(self) -> "str":
        return "pleroma.svg"

    @property
    def title(self) -> "str":
        return "Pleroma"

    @property
    def primary_color(self) -> "str":
        return "#FBA457"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pleroma</title>
     <path d="M6.36 0A1.868 1.868 0 004.49 1.868V24h5.964V0zm7.113
 0v12h4.168a1.868 1.868 0 001.868-1.868V0zm0 18.036V24h4.168a1.868
 1.868 0 001.868-1.868v-4.096Z" />
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
