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


class BlueskyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bluesky"

    @property
    def original_file_name(self) -> "str":
        return "bluesky.svg"

    @property
    def title(self) -> "str":
        return "Bluesky"

    @property
    def primary_color(self) -> "str":
        return "#0285FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bluesky</title>
     <path d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944
 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624
 6.479.815 2.736 3.713 3.66 6.383
 3.364.136-.02.275-.039.415-.056-.138.022-.276.04-.415.056-3.912.58-7.387
 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05
 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078a8.741 8.741 0 0
 1-.415-.056c.14.017.279.036.415.056 2.67.297 5.568-.628
 6.383-3.364.246-.828.624-5.79.624-6.478
 0-.69-.139-1.861-.902-2.206-.659-.298-1.664-.62-4.3 1.24C16.046 4.748
 13.087 8.687 12 10.8Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/FortAwesome/Font-Awesome/i'''

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
            "bsky",
        ]
