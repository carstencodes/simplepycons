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


class AmazonSqsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonsqs"

    @property
    def original_file_name(self) -> "str":
        return "amazonsqs.svg"

    @property
    def title(self) -> "str":
        return "Amazon SQS"

    @property
    def primary_color(self) -> "str":
        return "#FF4F8B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon SQS</title>
     <path d="m7.164 13.58 1.287-1.27a.425.425 0 0 0 .002-.603L7.166
 10.42l-.608.601.552.552H5.147v.852h1.97l-.557.55Zm9.82.04
 1.715-1.28a.427.427 0 0 0
 0-.682l-1.716-1.277-.515.682.686.51H15.44v.853h1.715l-.686.511ZM9.945
 12c0 .905-.156 1.758-.449 2.5a7.07 7.07 0 0 1 2.511-.445c.87 0
 1.74.148 2.51.445a6.855 6.855 0 0
 1-.448-2.5c0-.905.157-1.757.449-2.5-1.543.593-3.479.593-5.022 0
 .293.743.45 1.595.45 2.5Zm-2.1 4.136a.424.424 0 0 1 0-.602c.778-.774
 1.243-2.095 1.243-3.534 0-1.439-.465-2.76-1.244-3.534a.424.424 0 0 1
 0-.602.43.43 0 0 1 .607 0c1.662 1.65 5.45 1.65 7.113 0a.43.43 0 0 1
 .732.301.42.42 0 0 1-.126.301c-.778.774-1.243 2.095-1.243 3.534 0
 1.439.465 2.76 1.243 3.534a.424.424 0 0 1 0 .602.43.43 0 0 1-.606
 0c-1.662-1.65-5.451-1.65-7.113 0a.43.43 0 0 1-.607
 0Zm15.299-4.134c0-.397-.155-.77-.438-1.051a1.495 1.495 0 0
 0-1.058-.435c-.383 0-.766.145-1.058.435a1.481 1.481 0 0 0 0
 2.102c.583.58 1.532.58 2.116 0 .283-.28.438-.654.438-1.05Zm.168
 1.654a2.354 2.354 0 0 1-1.664.684 2.354 2.354 0 0 1-1.664-.684 2.33
 2.33 0 0 1 0-3.308 2.366 2.366 0 0 1 3.328 0 2.33 2.33 0 0 1 0
 3.308ZM3.85 12.012a1.491 1.491 0 0 0-1.496-1.487 1.493 1.493 0 0
 0-1.496 1.487c0 .397.155.77.437 1.051.566.561 1.551.561 2.116 0
 .283-.281.439-.654.439-1.051Zm.168 1.654a2.354 2.354 0 0 1-1.665.684
 2.355 2.355 0 0 1-1.664-.684 2.332 2.332 0 0 1 0-3.308 2.367 2.367 0
 0 1 3.329 0 2.33 2.33 0 0 1 0 3.308Zm14.367 4.7a9.034 9.034 0 0
 1-6.41 2.639 9.033 9.033 0 0
 1-6.41-2.638c-1.175-1.166-1.82-2.56-2.156-3.524l-.81.28c.364 1.047
 1.07 2.566 2.36 3.846a9.888 9.888 0 0 0 7.016 2.888 9.888 9.888 0 0 0
 7.016-2.888 10.234 10.234 0 0 0 2.43-3.848l-.812-.276a9.37 9.37 0 0
 1-2.224 3.522ZM3.407 9.158l-.81-.28c.52-1.484 1.358-2.851
 2.363-3.849a9.887 9.887 0 0 1 7.014-2.885 9.885 9.885 0 0 1 7.014
 2.885 10.497 10.497 0 0 1 2.43 3.85l-.809.279a9.628 9.628 0 0
 0-2.228-3.526 9.03 9.03 0 0 0-6.407-2.636 9.03 9.03 0 0 0-6.408
 2.636c-.914.909-1.681 2.161-2.159 3.526Z" />
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
        yield from [
            "Amazon Simple Queue Service",
            "AWS SQS",
            "AWS Simple Queue Service",
        ]
