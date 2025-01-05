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


class HearthisdotatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hearthisdotat"

    @property
    def original_file_name(self) -> "str":
        return "hearthisdotat.svg"

    @property
    def title(self) -> "str":
        return "hearthis.at"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>hearthis.at</title>
     <path d="M20.485 3.515C15.799-1.17 8.2-1.17 3.515 3.515c-4.687
 4.686-4.687 12.285 0 16.97 4.685 4.686 12.284 4.686 16.97 0
 4.687-4.685 4.687-12.284 0-16.97zm-5.81
 14.433c-.252.252-1.25.562-1.25-.012
 0-.573-.157-3.089-2.028-4.958-1.88-1.88-4.55-2.192-5.056-2.192-.506
 0-.331-1-.078-1.252.253-.253.558-.15 1.064-.15 0 0 3.445.464 5.326
 2.345 1.868 1.869 2.173 5.153 2.173 5.153 0 .463.102.813-.15
 1.066zm4.022-.509c-.36.36-1.786.803-1.786-.015
 0-.82-.224-4.41-2.893-7.079C11.335 7.662 7.524 7.217 6.8 7.217c-.723
 0-.473-1.426-.113-1.787.361-.36.799-.214 1.52-.214 0 0 4.918.663
 7.603 3.348 2.666 2.667 3.1 7.356 3.1 7.356 0 .658.147 1.158-.214
 1.52z" />
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
