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


class DvcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dvc"

    @property
    def original_file_name(self) -> "str":
        return "dvc.svg"

    @property
    def title(self) -> "str":
        return "DVC"

    @property
    def primary_color(self) -> "str":
        return "#13ADC7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DVC</title>
     <path d="M0 4.935a.295.295 0 0 1 .09-.223.256.256 0 0 1
 .201-.092h3.921c1.608.122 2.808.582 3.912 1.716 1.11 1.135 1.551
 2.422 1.692 4.078.135 1.594-.516 2.974-1.62 4.108a5.42 5.42 0 0
 1-1.818 1.28 5.316 5.316 0 0 1-2.166.431H.292a.28.28 0 0
 1-.202-.092.315.315 0 0 1-.069-.104.322.322 0 0
 1-.02-.123V4.935Zm2.508 8.84H4.05c.9 0 1.65-.326 2.244-.973a3.403
 3.403 0 0 0 .891-2.39c0-.942-.3-1.737-.89-2.383a2.935 2.935 0 0
 0-1.02-.734 2.88 2.88 0 0 0-1.225-.238H2.508zm12.064.062a.32.32 0 0 1
 .028.311l-2.324 5.056c-.063.122-.153.18-.273.18h-.162c-.12
 0-.21-.06-.276-.184l-2.28-4.993a.317.317 0 0 1 .033-.316 5.136 5.136
 0 0 0 .961-3.17c-.002-.088.133-.123.168-.042l1.44
 3.236h.098l1.494-3.354c.035-.078.16-.049.16.036 0 1.147.29 2.282.933
 3.24zm1.196.728c-1.14-1.128-1.668-2.496-1.668-4.108 0-1.622.525-2.996
 1.668-4.133a5.74 5.74 0 0 1 1.91-1.285 5.65 5.65 0 0 1 2.248-.423
 5.692 5.692 0 0 1 3.94 1.503c.164.153.167.306.017.453l-1.269
 1.31c-.14.128-.279.128-.408 0a3.21 3.21 0 0 0-2.199-.825c-.912
 0-1.67.325-2.28.981a3.267 3.267 0 0 0-.87 2.345c0 .908.27 1.68.882
 2.321a3.023 3.023 0 0 0 2.286.96 3.255 3.255 0 0 0
 2.181-.776c.15-.129.291-.123.42.015l1.272
 1.343c.141.141.135.285-.015.435a5.49 5.49 0 0 1-3.957 1.567 5.675
 5.675 0 0 1-2.245-.415 5.795 5.795 0 0 1-1.913-1.27z" />
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
            "Data Version Control",
        ]
