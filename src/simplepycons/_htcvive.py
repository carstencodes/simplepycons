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


class HtcViveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "htcvive"

    @property
    def original_file_name(self) -> "str":
        return "htcvive.svg"

    @property
    def title(self) -> "str":
        return "HTC Vive"

    @property
    def primary_color(self) -> "str":
        return "#00B2E3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HTC Vive</title>
     <path d="M16.225 19.046a14.3 14.3 0 0 1-4.222.642 14.3 14.3 0 0
 1-4.223-.642c-1.56-.505-2.525-2.066-2.203-3.672.596-2.938 2.111-5.508
 4.268-7.482a3.19 3.19 0 0 1 4.36 0c2.112 1.928 3.627 4.544 4.27
 7.482.275 1.606-.643 3.213-2.25 3.672m7.574-1.47L14.894 2.2a1.49 1.49
 0 0 0-1.33-.78h-3.076a1.49 1.49 0 0 0-1.331.78L.207
 17.577c-.276.505-.276 1.101 0 1.56l1.56 2.663c.276.504.78.78
 1.331.78h17.763c.551 0 1.056-.276
 1.331-.78l1.561-2.663c.321-.505.321-1.101.046-1.56" />
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
