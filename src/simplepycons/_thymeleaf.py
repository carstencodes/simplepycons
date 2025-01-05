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


class ThymeleafIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thymeleaf"

    @property
    def original_file_name(self) -> "str":
        return "thymeleaf.svg"

    @property
    def title(self) -> "str":
        return "Thymeleaf"

    @property
    def primary_color(self) -> "str":
        return "#005F0F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thymeleaf</title>
     <path d="M1.727 0C.782 0 .02.761.02 1.707v20.586C.02 23.24.782 24
 1.727 24h20.546c.945 0 1.707-.761 1.707-1.707V1.707C23.98.76 23.218 0
 22.273 0H1.727zm18.714 3.273c-1.861 3.694-3.3 7.627-5.674
 11.046-1.064 1.574-2.329 3.163-4.16
 3.86-1.31.552-2.936.337-3.98-.647-.628-.523-.54-1.43-.173-2.075.96-1.224
 2.34-2.02 3.59-2.915 3.842-2.625 7.446-5.654 10.397-9.27zm-1.693
 1.25c-2.503 2.751-5.381 5.16-8.452
 7.269l-.003.002-.003.003c-1.327.979-2.835 1.824-3.993
 3.114-.349.333-.583 1.042-.537
 1.481-.622-1.043-.8-2.614-.257-3.74.526-1.19 1.742-1.807 2.876-2.292
 3.757-1.353 6.695-2.926 10.369-5.836z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/thymeleaf/thymeleaf-org/bl
ob/0427d4d4c6f08d3a1fbed3bc90ceeebcf094b532/artwork/thymeleaf%202016/t'''

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
