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


class DataikuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dataiku"

    @property
    def original_file_name(self) -> "str":
        return "dataiku.svg"

    @property
    def title(self) -> "str":
        return "Dataiku"

    @property
    def primary_color(self) -> "str":
        return "#2AB1AC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dataiku</title>
     <path d="M12 0a12 12 0 1 0 12 12A12 12 0 0 0 12 0zm6.527
 15.34H12.5v-.934h6.026zm-.739-8.73s-.412.543-.193 1.995c.41
 2.724-1.02 5.15-3.56 5.15h-1.87s-1.835-.092-2.933 1.01c-3.263
 3.269-4.04 4.116-4.274
 4.233-.15.08-.188-.093-.188-.093l9.644-11.891c-.203-2.145 2.34-2.715
 3.278-1.13l.884-.248zm-1.599-.614a.476.476 0 1 0 .47.474.476.476 0 0
 0-.47-.474z" />
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
