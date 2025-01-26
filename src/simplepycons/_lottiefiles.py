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


class LottiefilesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lottiefiles"

    @property
    def original_file_name(self) -> "str":
        return "lottiefiles.svg"

    @property
    def title(self) -> "str":
        return "LottieFiles"

    @property
    def primary_color(self) -> "str":
        return "#00DDB3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LottieFiles</title>
     <path d="M17.928 0H6.072A6.076 6.076 0 0 0 0 6.073v11.854A6.076
 6.076 0 0 0 6.073 24h11.854A6.076 6.076 0 0 0 24 17.927V6.073A6.076
 6.076 0 0 0 17.927 0m1.42 7.013a1.4 1.4 0 0
 1-.26.39c-.11.11-.24.2-.39.26-.14.06-.3.09-.45.09-2.511 0-3.482
 1.53-4.792 4.042l-.8 1.51c-1.231 2.382-2.762 5.323-6.894 5.323-.31
 0-.62-.12-.84-.35a1.188 1.188 0 0 1 .84-2.031c2.511 0 3.482-1.53
 4.792-4.042l.8-1.51c1.231-2.382 2.762-5.323 6.894-5.323q.24 0
 .45.09c.14.06.27.15.39.26.11.11.2.24.26.39a1.17 1.17 0 0 1 0 .9" />
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
