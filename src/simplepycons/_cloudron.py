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


class CloudronIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudron"

    @property
    def original_file_name(self) -> "str":
        return "cloudron.svg"

    @property
    def title(self) -> "str":
        return "Cloudron"

    @property
    def primary_color(self) -> "str":
        return "#03A9F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudron</title>
     <path d="M12.016.86c-2.676-.004-5.353.182-6.002.562C4.714
 2.182.002 10.46 0 11.984c-.002 1.525 4.69 9.813 5.986 10.577
 1.297.764 10.701.778 12 .017 1.3-.76 6.012-9.038
 6.014-10.562.002-1.525-4.69-9.813-5.986-10.577-.649-.382-3.323-.576-5.998-.58zm-.268
 4.363h2.38c.85 0 1.534.682 1.534 1.53V9.23a1.53 1.53 0 0 1-1.533
 1.533h-2.381c-.127
 0-.25-.018-.367-.047l.002.047v2.476l-.002.047c.117-.029.24-.047.367-.047h2.38a1.53
 1.53 0 0 1 1.534 1.533v2.475c0 .849-.684 1.531-1.533
 1.531h-2.381a1.529 1.529 0 0 1-1.533-1.53V14.77l.002-.046a1.538 1.538
 0 0 1-.365.045H7.469a1.527 1.527 0 0
 1-1.532-1.532v-2.476c0-.849.683-1.532 1.532-1.532h2.383c.126 0
 .248.017.365.045l-.002-.046V6.754c0-.849.684-1.531 1.533-1.531z" />
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
