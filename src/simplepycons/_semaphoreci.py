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


class SemaphoreCiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "semaphoreci"

    @property
    def original_file_name(self) -> "str":
        return "semaphoreci.svg"

    @property
    def title(self) -> "str":
        return "Semaphore CI"

    @property
    def primary_color(self) -> "str":
        return "#19A974"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Semaphore CI</title>
     <path d="m21.50314 13.2549-4.15781-4.22828a3.03814 3.03814 0 0
 0-4.3591 0L9.6943 12.374a1.20701 1.20701 0 0 1-1.7213
 0l-1.63096-1.6587 4.1578-4.22866a6.53247 6.53247 0 0 1 9.34234 0L24
 10.71531zM8.82879 19.47925a6.52947 6.52947 0 0 1-4.67098-1.9657L0
 13.295l2.48674-2.52872 4.15744 4.21816a3.05613 3.05613 0 0 0 4.3591
 0l3.29191-3.34814a1.20701 1.20701 0 0 1 1.7213 0l1.63097
 1.6587-4.14732 4.22866a6.5186 6.5186 0 0 1-4.67135 1.95558z" />
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
