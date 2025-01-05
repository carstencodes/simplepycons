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


class TwoFasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "2fas"

    @property
    def original_file_name(self) -> "str":
        return "2fas.svg"

    @property
    def title(self) -> "str":
        return "2FAS"

    @property
    def primary_color(self) -> "str":
        return "#EC1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>2FAS</title>
     <path d="M12 0c-.918 0-1.833.12-2.72.355L4.07 1.748a2.64 2.64 0 0
 0-1.96 2.547v9.115a7.913 7.913 0 0 0 3.552 6.606l5.697 3.765a1.32
 1.32 0 0 0 1.467-.008l5.572-3.752a7.931 7.931 0 0 0
 3.493-6.57V4.295a2.638 2.638 0 0 0-1.961-2.547L14.72.355A10.594
 10.594 0 0 0 12 0ZM7.383 5.4h9.228c.726 0 1.32.594 1.32 1.32 0
 .734-.587 1.32-1.32 1.32H7.383c-.727 0-1.32-.593-1.32-1.32
 0-.726.593-1.32 1.32-1.32zM7.38 9.357h3.299c.727 0 1.32.595 1.32
 1.32a1.32 1.32 0 0 1-1.318 1.32H7.38c-.726 0-1.32-.592-1.32-1.32
 0-.725.594-1.32 1.32-1.32zm0 3.96c.727 0 1.32.593 1.32 1.32 0
 .727-.586 1.318-1.32 1.318-.726 0-1.32-.592-1.32-1.318
 0-.727.594-1.32 1.32-1.32z" />
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
