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


class ResendIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "resend"

    @property
    def original_file_name(self) -> "str":
        return "resend.svg"

    @property
    def title(self) -> "str":
        return "Resend"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Resend</title>
     <path d="M2.023 0v24h5.553v-8.434h2.998L15.326
 24h6.65l-5.372-9.258a7.652 7.652 0 0 0 3.316-3.016c.709-1.21
 1.062-2.57 1.062-4.08
 0-1.462-.353-2.767-1.062-3.91-.709-1.165-1.692-2.079-2.95-2.742C15.737.331
 14.355 0 12.823 0Zm5.553 4.87h4.219c.731 0 1.349.125
 1.851.376.526.252.925.618 1.2 1.098.274.457.412.994.412 1.611S15.132
 9.12 14.88 9.6c-.229.48-.572.856-1.03
 1.13-.434.252-.948.38-1.542.38H7.576Z" />
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
