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


class GoogleFitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlefit"

    @property
    def original_file_name(self) -> "str":
        return "googlefit.svg"

    @property
    def title(self) -> "str":
        return "Google Fit"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Fit</title>
     <path d="M23.218
 4.868c-1.235-2.194-3.927-3.356-6.378-2.843-1.11.243-2.173.774-2.979
 1.583-.622.613-1.242 1.229-1.864
 1.841-.915-.91-1.788-1.937-2.882-2.648a5.98 5.98 0 0
 0-3.904-.845c-4.757.578-6.936 6.346-3.615 9.85 3.481 3.418 6.937
 6.863 10.413 10.288 3.291-3.251 6.573-6.51 9.871-9.752 2.132-1.831
 2.8-5.026 1.338-7.474zM6.162
 11.223c-.692-.755-1.511-1.404-2.141-2.208-.821-1.218-.158-3.012
 1.26-3.397.781-.256 1.683-.031 2.279.527.627.609 1.236 1.237 1.866
 1.843l.005.006a414.706 414.706 0 0 0-3.269 3.229zm5.846
 5.758a3300.079 3300.079 0 0 1-3.255-3.22c2.555-2.516 5.103-5.042
 7.65-7.566.393-.394.93-.646 1.487-.673 2.086-.154 3.285 2.372 1.801
 3.866-2.549 2.542-5.121 5.062-7.683 7.593z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
