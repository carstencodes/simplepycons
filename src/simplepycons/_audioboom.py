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


class AudioboomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "audioboom"

    @property
    def original_file_name(self) -> "str":
        return "audioboom.svg"

    @property
    def title(self) -> "str":
        return "Audioboom"

    @property
    def primary_color(self) -> "str":
        return "#007CE2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Audioboom</title>
     <path d="M12 24C5.373 24 0 18.627 0 12S5.373 0 12 0s12 5.373 12
 12-5.373 12-12 12zM7.425 3.214c-.621 0-1.125.503-1.125 1.124v6a1.124
 1.124 0 0 0 2.25 0v-6c0-.62-.504-1.124-1.125-1.124zm0 9.314c-.621
 0-1.125.503-1.125 1.125v6a1.124 1.124 0 0 0 2.25
 0v-6c0-.622-.504-1.125-1.125-1.125zm4.152-6.856c-.621
 0-1.125.504-1.125 1.125v10.388a1.124 1.124 0 0 0 2.25
 0V6.797c0-.621-.504-1.125-1.125-1.125zm4.151 6.856c-.62
 0-1.124.503-1.124 1.125v1.056a1.124 1.124 0 1 0 2.249
 0v-1.056c0-.622-.504-1.125-1.125-1.125zm0-4.37c-.62 0-1.124.503-1.124
 1.124v1.056a1.124 1.124 0 0 0 2.249
 0V9.282c0-.62-.504-1.124-1.125-1.124zm4.152 2.422c-.62
 0-1.124.503-1.124 1.124v.574a1.124 1.124 0 1 0 2.249
 0v-.574c0-.62-.504-1.124-1.125-1.124Z" />
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
