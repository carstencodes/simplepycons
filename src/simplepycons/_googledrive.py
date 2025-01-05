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


class GoogleDriveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googledrive"

    @property
    def original_file_name(self) -> "str":
        return "googledrive.svg"

    @property
    def title(self) -> "str":
        return "Google Drive"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Drive</title>
     <path d="M12.01 1.485c-2.082 0-3.754.02-3.743.047.01.02 1.708
 3.001 3.774 6.62l3.76 6.574h3.76c2.081 0 3.753-.02
 3.742-.047-.005-.02-1.708-3.001-3.775-6.62l-3.76-6.574zm-4.76
 1.73a789.828 789.861 0 0 0-3.63 6.319L0 15.868l1.89 3.298 1.885 3.297
 3.62-6.335 3.618-6.33-1.88-3.287C8.1 4.704 7.255 3.22 7.25
 3.214zm2.259 12.653-.203.348c-.114.198-.96 1.672-1.88 3.287a423.93
 423.948 0 0 1-1.698 2.97c-.01.026 3.24.042
 7.222.042h7.244l1.796-3.157c.992-1.734 1.85-3.23
 1.906-3.323l.104-.167h-7.249z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/drive/web/brand'''

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
