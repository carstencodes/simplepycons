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


class RedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "red"

    @property
    def original_file_name(self) -> "str":
        return "red.svg"

    @property
    def title(self) -> "str":
        return "Red"

    @property
    def primary_color(self) -> "str":
        return "#B32629"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Red</title>
     <path d="M12 6.679V0L8.655 4.945Zm0 1.976v6.69l7.673-4L16.327
 6.4zm0-1.976 3.345-1.734L12 0Zm8.655 6.133L12 17.322V24l12-6.242ZM12
 24v-6.679l-8.655-4.509L0 17.758ZM4.327 11.345l7.673 4v-6.69L7.673
 6.4Z" />
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
